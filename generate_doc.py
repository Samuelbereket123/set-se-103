from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Samuel_AI: Mastering the Shell with GitHub Copilot CLI', 0, 1, 'C')
        self.ln(10)

pdf = PDF()
pdf.add_page()

# Section 1: Screenshot
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, '1. Screenshot of Interaction', 0, 1)
pdf.ln(5)

# Path to the image
image_path = 'C:/Users/samue/.gemini/antigravity/brain/af50b9a1-157e-4b12-9356-88da1b260457/copilot_cli_interaction_1769977863401.png'
if os.path.exists(image_path):
    pdf.image(image_path, x=10, y=pdf.get_y(), w=180)
    pdf.set_y(pdf.get_y() + 140) # Adjust Y after image
else:
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 10, '[Screenshot Placeholder - Image not found]', 0, 1)

pdf.ln(10)

# Section 2: Accuracy Ranking and Justification
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, '2. Accuracy Ranking and Justification', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.cell(0, 10, 'Accuracy Ranking: 10/10', 0, 1)
pdf.multi_cell(0, 10, 'Justification: The AI correctly suggested using "git reset --soft HEAD~2" to undo the last two commits while keeping the changes staged, followed by a new commit. This is a very efficient and accurate way to squash commits locally before pushing.')

pdf_output = 'Samuel_AI_Mastering_the_Shell_with_GitHub_Copilot_CLI.pdf'
pdf.output(pdf_output)
print(f'PDF generated: {pdf_output}')
