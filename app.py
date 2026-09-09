from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PAFDemoServer")


@mcp.tool()
def health_check():
    return {
        "status": "UP",
        "server": "PAFDemoServer"
    }


@mcp.tool()
def get_invoice_status(invoice_id: str):
    return {
        "invoice_id": invoice_id,
        "status": "Pending Approval",
        "amount": 50000
    }


@mcp.tool()
def get_po_status(po_number: str):
    return {
        "po_number": po_number,
        "status": "Approved"
    }


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )