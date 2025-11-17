# Purchase Requisition System Prototype
# Global variable for generating unique requisition IDs
requisition_counter = 10000

def generate_requisition_id():
    """Task 1: Generate unique requisition ID"""
    global requisition_counter
    requisition_counter += 1
    return requisition_counter

def collect_requisition_items():
    """Collect requisition items information"""
    items = []
    print("\nPlease enter requisition items (type 'done' to finish):")
    
    while True:
        item_name = input("Item name: ")
        if item_name.lower() == 'done':
            break
        
        try:
            item_cost = float(input("Item cost ($): "))
            items.append({"name": item_name, "cost": item_cost})
            print(f"Added: {item_name} - ${item_cost}")
        except ValueError:
            print("Error: Please enter a valid number!")
    
    return items

def task1_collect_info():
    """Task 1: Collect staff information and generate requisition ID"""
    print("=" * 50)
    print("Purchase Requisition System - Information Collection")
    print("=" * 50)
    
    # Collect basic information
    date = input("Enter date (DD/MM/YYYY): ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")
    
    # Generate unique requisition ID
    requisition_id = generate_requisition_id()
    
    # Collect items information
    items = collect_requisition_items()
    
    # Return all information
    requisition_data = {
        "date": date,
        "staff_id": staff_id,
        "staff_name": staff_name,
        "requisition_id": requisition_id,
        "items": items
    }
    
    print(f"\nRequisition ID {requisition_id} has been generated!")
    return requisition_data

def task2_calculate_total(requisition_data):
    """Task 2: Calculate requisition total amount"""
    print("\n" + "=" * 30)
    print("Calculate Requisition Total")
    print("=" * 30)
    
    total = 0
    items = requisition_data["items"]
    
    print("Requisition Items List:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item['name']}: ${item['cost']:.2f}")
        total += item["cost"]
    
    requisition_data["total"] = total
    print(f"\nRequisition Total: ${total:.2f}")
    
    return total

def generate_approval_ref(requisition_data):
    """Generate approval reference number"""
    staff_id = requisition_data["staff_id"]
    req_id_str = str(requisition_data["requisition_id"])
    last_three = req_id_str[-3:]  # Get last three digits of requisition ID
    
    return staff_id + last_three

def task3_approval_decision(requisition_data):
    """Task 3: Approval decision making"""
    print("\n" + "=" * 30)
    print("Approval Decision Processing")
    print("=" * 30)
    
    total = requisition_data["total"]
    
    # Default status is Pending
    requisition_data["status"] = "Pending"
    requisition_data["approval_ref"] = "Not available"
    
    # Auto-approval logic: total < $500 gets auto-approved
    if total < 500:
        requisition_data["status"] = "Approved"
        requisition_data["approval_ref"] = generate_approval_ref(requisition_data)
        print("Auto-approved: Requisition total is less than $500")
        print(f"Generated approval reference: {requisition_data['approval_ref']}")
    
    else:
        # Manager manual approval required
        print(f"Requisition Total: ${total:.2f} - Requires manager approval")
        print("\nManager Approval Options:")
        print("1. Approve")
        print("2. Not Approve")
        print("3. Keep Pending")
        
        try:
            manager_decision = input("Enter your choice (1/2/3): ")
            
            if manager_decision == "1":
                requisition_data["status"] = "Approved"
                requisition_data["approval_ref"] = generate_approval_ref(requisition_data)
                print(f"Requisition Approved! Reference: {requisition_data['approval_ref']}")
            elif manager_decision == "2":
                requisition_data["status"] = "Not approved"
                print("Requisition Not Approved!")
            else:
                print("Requisition status remains: Pending")
                
        except Exception as e:
            print(f"Approval processing error: {e}")
    
    return requisition_data

def task4_display_requisition(requisition_data):
    """Task 4: Display requisition information"""
    print("\n" + "=" * 50)
    print("Purchase Requisition Details")
    print("=" * 50)
    
    print(f"Date: {requisition_data['date']}")
    print(f"Requisition ID: {requisition_data['requisition_id']}")
    print(f"Staff ID: {requisition_data['staff_id']}")
    print(f"Staff Name: {requisition_data['staff_name']}")
    print(f"Total: ${requisition_data['total']:.2f}")
    print(f"Status: {requisition_data['status']}")
    print(f"Approval Reference Number: {requisition_data['approval_ref']}")
    
    # Display items details
    print("\nRequisition Items Details:")
    for i, item in enumerate(requisition_data["items"], 1):
        print(f"  {i}. {item['name']}: ${item['cost']:.2f}")
    
    print("=" * 50)

def main():
    """Main function - coordinates all tasks"""
    print("Purchase Requisition System Prototype")
    print("Version 1.0")
    
    # List to store multiple requisitions
    all_requisitions = []
    
    while True:
        print("\nMain Menu:")
        print("1. Create New Requisition")
        print("2. View All Requisitions")
        print("3. Exit System")
        
        choice = input("Please choose (1/2/3): ")
        
        if choice == "1":
            # Execute all tasks
            requisition_data = task1_collect_info()      # Task 1
            total = task2_calculate_total(requisition_data)  # Task 2
            approved_data = task3_approval_decision(requisition_data)  # Task 3
            task4_display_requisition(approved_data)     # Task 4
            
            # Save requisition data
            all_requisitions.append(approved_data)
            
        elif choice == "2":
            if not all_requisitions:
                print("\nNo requisition records found!")
            else:
                print(f"\nTotal {len(all_requisitions)} requisitions:")
                for i, req in enumerate(all_requisitions, 1):
                    print(f"\nRequisition #{i}:")
                    task4_display_requisition(req)
                    
        elif choice == "3":
            print("Thank you for using the Purchase Requisition System!")
            break
            
        else:
            print("Invalid choice, please try again!")

# Test function
def test_system():
    """Test system functionality"""
    print("Running system tests...")
    
    # Test data
    test_data = {
        "date": "03/04/2024",
        "staff_id": "FN19",
        "staff_name": "John Paul",
        "requisition_id": 10001,
        "items": [
            {"name": "Office Supplies", "cost": 200},
            {"name": "Printer Paper", "cost": 250}
        ]
    }
    
    print("\nTesting Auto-approval (< $500):")
    test_data["total"] = 450
    approved_test = task3_approval_decision(test_data.copy())
    task4_display_requisition(approved_test)
    
    print("\nTesting Manager Approval (>= $500):")
    test_data["total"] = 1000
    test_data["requisition_id"] = 10002
    test_data["staff_id"] = "FN20"
    test_data["staff_name"] = "Tracy Brown"
    pending_test = task3_approval_decision(test_data.copy())
    task4_display_requisition(pending_test)

if __name__ == "__main__":
    # Option to run test or main system
    run_test = input("Run test mode? (y/n): ").lower()
    
    if run_test == 'y':
        test_system()
    else:
        main()