#!/usr/bin/env python3
"""
Streamlit web interface for the Financial Research Agent
"""
import streamlit as st
import asyncio
import os
import sys
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, '/app/src')
sys.path.insert(0, '/app')

st.set_page_config(
    page_title="Financial Research Agent",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Financial Research Agent")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("🔧 Configuration")
    api_key_status = "✅ Configured" if os.getenv('OPENAI_API_KEY') else "❌ Missing"
    st.write(f"**OpenAI API Key:** {api_key_status}")
    
    st.header("📋 Recent Reports")
    reports_dir = Path("/tmp/financial-agent-reports")
    if reports_dir.exists():
        reports = list(reports_dir.glob("*.txt"))
        for report in reports[-5:]:  # Last 5 reports
            if st.button(f"📄 {report.stem}", key=f"report_{report.stem}"):
                with open(report, 'r') as f:
                    st.session_state['display_report'] = f.read()
    else:
        st.write("No reports found yet")

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.header("🔍 Financial Analysis")
    
    # Query input
    query = st.text_area(
        "Enter your financial research query:",
        height=100,
        placeholder="e.g., Analyze Apple's most recent quarter"
    )
    
    # Example queries
    st.write("**Example Queries:**")
    examples = [
        "Analyze Apple's most recent quarter",
        "Write a report on Tesla's financial performance", 
        "Research Microsoft's competitive position in cloud services",
        "Evaluate Amazon's e-commerce growth trends",
        "Analyze NVIDIA's AI chip market position"
    ]
    
    for example in examples:
        if st.button(f"📌 {example}", key=f"example_{hash(example)}"):
            st.session_state['query'] = example
            query = example
    
    # Run analysis button
    if st.button("🚀 Run Analysis", type="primary", disabled=not query):
        if not os.getenv('OPENAI_API_KEY'):
            st.error("❌ OpenAI API key not configured!")
        else:
            with st.spinner("🔄 Running financial analysis..."):
                try:
                    # Import and run the financial research manager
                    from financial_research_agent.manager import FinancialResearchManager
                    from agents.mcp import MCPServerSse
                    
                    async def run_analysis():
                        mgr = FinancialResearchManager()
                        mcp_server = MCPServerSse(
                            name="Web Interface Server",
                            params={"url": "http://localhost:8000/sse"}
                        )
                        await mgr.run(query, mcp_server)
                        
                        # Read the generated report
                        report_file = Path("/app/financial_report.txt")
                        if report_file.exists():
                            return report_file.read_text()
                        return "Report generated but file not found."
                    
                    # Run the analysis
                    report = asyncio.run(run_analysis())
                    st.session_state['latest_report'] = report
                    st.success("✅ Analysis complete!")
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    if "quota" in str(e).lower():
                        st.warning("💡 This looks like an OpenAI quota issue. Please check your billing at https://platform.openai.com/account/billing")

with col2:
    st.header("📄 Generated Report")
    
    # Display report
    if 'latest_report' in st.session_state:
        st.markdown(st.session_state['latest_report'])
    elif 'display_report' in st.session_state:
        st.markdown(st.session_state['display_report'])
    else:
        st.info("👈 Enter a query and click 'Run Analysis' to generate a financial report.")

# Footer
st.markdown("---")
st.markdown("**📊 Financial Research Agent** - Powered by OpenAI Agents SDK")

# Auto-refresh option
if st.checkbox("🔄 Auto-refresh every 30 seconds"):
    import time
    time.sleep(30)
    st.rerun()