test_cases = int(input())

for _ in range(test_cases):
    system_doc_list = []
    system_ship_list = []
    system_doc, system_ship = map(int,input().split())
    for i in range(system_doc):
        system_doc_list.append(input())
    for i in range(system_ship):
        system_ship_list.append(input())
    
    for part in system_doc_list:
        if part not in system_ship_list:
            print("parts to check: ",part)