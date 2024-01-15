#!/bin/bash

# File paths for various outputs
system_info_file="system_info.txt"
data_collection_output="data_collection_output.txt"
data_cleaning_output="data_cleaning_output.txt"
nlg_output="nlg_output.txt"
decision_logic_output="decision_logic_output.txt"

# Function to gather hardware information
gather_hardware_info() {
    echo "Gathering hardware information..."
    # Example: lshw > $system_info_file
}

# Function to gather software information
gather_software_info() {
    echo "Gathering software information..."
    # Example: dpkg -l > $system_info_file
}

# Function to call Python script for data collection
call_data_collection() {
    echo "Running data collection Python script..."
    python3 data_collection_script.py > $data_collection_output
}

# Function to call Python script for data cleaning
call_data_cleaning() {
    echo "Running data cleaning Python script..."
    python3 data_cleaning_script.py > $data_cleaning_output
}

# Function to call Python script for NLG
call_nlg() {
    echo "Running NLG Python script..."
    python3 nlg_script.py > $nlg_output
}

# Function to call Python script for decision logic
call_decision_logic() {
    echo "Running decision logic Python script..."
    python3 decision_logic_script.py > $decision_logic_output
}

# Main loop for user interaction
while true; do
    read -p "> " user_input
    case "$user_input" in
        "Gather Hardware Info")
            gather_hardware_info
            ;;
        "Gather Software Info")
            gather_software_info
            ;;
        "Collect Data")
            call_data_collection
            ;;
        "Clean Data")
            call_data_cleaning
            ;;
        "Generate NLG")
            call_nlg
            ;;
        "Decision Logic")
            call_decision_logic
            ;;
        "Exit")
            echo "Exiting script."
            break
            ;;
        *)
            echo "Invalid option. Please choose a valid command."
            ;;
    esac
done

