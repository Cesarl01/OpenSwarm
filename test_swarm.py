from swarm import create_agency

agency = create_agency()
print("Agency created successfully. Sending message...")
response = agency.get_response_sync("Hola, ¿quién eres y qué puedes hacer?")
print("-" * 20)
print("Response from OpenSwarm:")
print(response)
print("-" * 20)
