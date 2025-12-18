#!/usr/bin/env python3
"""Check Strands Agent API"""

try:
    from strands import Agent
    import inspect
    
    print("Strands Agent methods:")
    for name, method in inspect.getmembers(Agent, predicate=inspect.ismethod):
        if not name.startswith('_'):
            print(f"  - {name}")
    
    print("\nStrands Agent attributes:")
    agent = Agent()
    for attr in dir(agent):
        if not attr.startswith('_'):
            print(f"  - {attr}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
