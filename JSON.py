import JSON
empolyee_data =[{"fname":"abc", "lname":"xyz", "id": 1}, 
                {"fname":"abc", "lname":"xyz", "id": 2}]
                
                
            
            
JSON_data = json.dumps(employee_data, indent=2)
print(json_data)        
