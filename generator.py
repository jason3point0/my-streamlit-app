from openai import OpenAI
client = OpenAI()

def generate_cover_letter(job_description):

    prompt = f'''\n    Generate a professional offshore cover letter for Jason Bent.\n    Highlight Stage 4 rigging, IRATA L2, hydraulic bolting and FPSO experience.\n\n    Job Description:\n    {job_description}\n    '''

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content