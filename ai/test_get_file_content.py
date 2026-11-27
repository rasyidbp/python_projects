
from functions.get_file_content import get_file_content


# Test 1: Large file (should truncate)
result = get_file_content("calculator", "lorem.txt")

print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")


# Test 2: Read main.py
print("\n--- main.py ---")
print(get_file_content("calculator", "main.py"))


# Test 3: Read calculator.py
print("\n--- pkg/calculator.py ---")
print(get_file_content("calculator", "pkg/calculator.py"))


# Test 4: Try accessing a file outside the working directory
print("\n--- /bin/cat ---")
print(get_file_content("calculator", "/bin/cat"))


# Test 5: Try accessing a nonexistent file
print("\n--- does_not_exist.py ---")
print(get_file_content("calculator", "pkg/does_not_exist.py"))

