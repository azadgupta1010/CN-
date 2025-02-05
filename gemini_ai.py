from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv

load_dotenv()


def create_gemini_ai():
    # Initialize Gemini Pro model
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.7,
        convert_system_message_to_human=True
    )

    # Configure memory
    memory = ConversationBufferMemory()

    # Create conversation chain
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False
    )
    return conversation


if __name__ == "__main__":
    ai = create_gemini_ai()
    print("CN🤍: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("CN🤍: Goodbye!")
            break
        response = ai.invoke(user_input)
        print(f"CN🤍: {response['response']}")