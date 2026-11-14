
    from dotenv import
    load_dotenv
    from
    langchain_core.prompts
    import PromptTemplate
    from
    langchain_google_genai
    import
    ChatGoogleGenerativeAI

    load_dotenv()

    model =
    ChatGoogleGenerativeAI(
    model="gemini-1.5-flash
    ")

    # Step 1: First model
    call
    prompt1 = "List 3 key
    emotional highlights of
    a school farewell."
    result =
    model.invoke(prompt1)

    # Step 2: Use the
    output of step 1 in the
    second template
    template2 =
    PromptTemplate(
        template="Write a
        cohesive summary
        for my school
        farewell from these
        points: {text}",
        input_variables=["t
        ext"],
    )

    prompt2 =
    template2.invoke({"text
    ": result.content})
    result1 =
    model.invoke(prompt2)

    print(result1.content)
