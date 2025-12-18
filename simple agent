

#!/usr/bin/env python3
"""Simple, guaranteed-working MT Agent"""

import sys
import os

# Add the my_agent directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'my_agent'))

def main():
    print("🚀 MT AGENT - Restaurant Assistant")
    print("=" * 50)
    print("💬 Ask me anything about restaurants, menus, cooking!")
    print("🔧 Commands: 'help', 'quit'")
    print("=" * 50)
    
    try:
        from my_agent.agent import Agent
        agent = Agent()
        
        print("✅ Agent ready! Start asking questions...")
        
        while True:
            try:
                user_input = input("\n🍽️  Restaurant Assistant> ")
                
                if user_input.lower().strip() in ['quit', 'exit', 'q', 'bye']:
                    print("👋 Thanks for using MT Agent! Goodbye!")
                    break
                elif user_input.lower().strip() in ['help', 'h']:
                    print("📋 How to use MT Agent:")
                    print("  • Ask about menus: 'How do I plan a menu?'")
                    print("  • Ask about cooking: 'Give me cooking tips'")
                    print("  • Ask about service: 'How to improve customer service?'")
                    print("  • Ask about business: 'Restaurant success tips?'")
                    print("  • Say hello: 'Hello!' or 'Hi!'")
                    print("  • Get help: 'help'")
                    print("  • Exit: 'quit'")
                elif user_input.strip() == "":
                    print("💡 Please ask me a question! Try 'help' for examples.")
                else:
                    print("🔄 Let me help you with that...")
                    agent._process_user_question(user_input)
                    
            except KeyboardInterrupt:
                print("\n👋 Thanks for using MT Agent! Goodbye!")
                break
            except Exception as e:
                print(f"❌ Sorry, I had an error: {e}")
                print("💡 Try asking a different question or type 'help'")
                
    except Exception as e:
        print(f"❌ Failed to start agent: {e}")
        print("💡 Please check if all files are in place")

if __name__ == "__main__":
    main()
