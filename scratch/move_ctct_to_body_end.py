import glob
import re

html_files = glob.glob('es/**/*.html', recursive=True) + glob.glob('en/**/*.html', recursive=True)

ctct_block = """  <!-- Begin Constant Contact Active Forms -->
  <script> var _ctct_m = "a79e89c0998befa80793c5464469c842"; </script>
  <script id="signupScript" src="https://static.ctctcdn.com/js/signup-form-widget/current/signup-form-widget.min.js" async defer></script>
  <!-- End Constant Contact Active Forms -->"""

updated_count = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove existing CTCT Active Forms blocks anywhere in the file
    new_content = re.sub(r'[\t ]*<!-- Begin Constant Contact Active Forms -->[\s\S]*?<!-- End Constant Contact Active Forms -->\s*', '', content)
    
    # Also clean up orphaned script tags if any
    new_content = re.sub(r'[\t ]*<script>\s*var _ctct_m = [\s\S]*?</script>\s*', '', new_content)
    new_content = re.sub(r'[\t ]*<script id="signupScript"[\s\S]*?></script>\s*', '', new_content)

    # Insert CTCT block right before </body>
    if '</body>' in new_content:
        new_content = new_content.replace('</body>', ctct_block + '\n</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_count += 1
        print(f"Updated CTCT script placement in: {filepath}")
    else:
        print(f"Warning: </body> not found in {filepath}")

print(f"\nTotal files updated: {updated_count}")
