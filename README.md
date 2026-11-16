# DownloadingGoogleFormsData.py

This script extracts email addresses from a specific Google Spreadsheet (likely containing Google Form response data) using the `ezsheets` library. Here's what it does:

1. **Connects to a Google Sheet** via a hardcoded URL and accesses the first worksheet.
2. **Prints the sheet dimensions** (number of columns and rows).
3. **Searches the header row** (row 1) for a column title containing `"email"` (case-sensitive).
4. **Iterates down that column** starting at row 2, printing each non-empty cell value.
5. **Stops at the first blank cell** in that column and exits both loops.

**Assumptions & behavior:**
- Row 1 contains column headers; row 2+ contains data.
- Emails are listed contiguously from the top of the identified column.
- The script halts output upon encountering the first empty cell in that column.
- The Google Sheet URL and column structure are fixed; changes to the header text or data layout will cause the script to skip or fail.

In short: *It automates pulling an email list from a Google Form responses sheet, stopping at the first gap in the list.*