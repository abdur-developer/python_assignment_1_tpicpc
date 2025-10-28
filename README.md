# 🐍 Basic to Advanced Python Workshop – Assignment 1

**Based on:** Class 1–4  
**Topics Covered:** Variables, Input/Output, Arithmetic, Condition, Loops, Functions & Modules

---

## 🎯 Objective

এই অ্যাসাইনমেন্টের মাধ্যমে আপনি Python-এর বেসিক সিনট্যাক্স ভালোভাবে ঝালিয়ে নিতে পারবেন —  
ইনপুট নেওয়া, হিসাব করা, শর্ত দেওয়া, লুপ চালানো, এবং ফাংশন ব্যবহার করা অনুশীলন করবেন।

---

## 🧩 Assignment Problems

---

### 🟢 Problem 1: Simple Calculator ➕➖✖️➗  
**Topic:** Input, Variables, Arithmetic Operators  

**🧠 Task:**  
একটি প্রোগ্রাম লিখুন যা ইউজারের কাছ থেকে দুইটি সংখ্যা ইনপুট নেবে,  
তারপর নিচের চারটি কাজ সম্পন্ন করবে —  
- Addition  
- Subtraction  
- Multiplication  
- Division  

**💡 Hint:**  
- ইনপুট নিন `float(input())` ব্যবহার করে  
- অপারেটরগুলো ব্যবহার করুন: `+`, `-`, `*`, `/`  
- প্রতিটি ফলাফল `print()` দিয়ে দেখান  

**🧩 Example:**
Enter first number: 10
Enter second number: 5
Addition: 15.0
Subtraction: 5.0
Multiplication: 50.0
Division: 2.0

pgsql
Copy code

**🔍 Trick:**  
প্রতিবার `input()` দিলে string আসে — তাই `float()` ব্যবহার করুন যেন সংখ্যার মতো কাজ করে।

---

### 🟢 Problem 2: Area of a Circle ⚪  
**Topic:** Variables, Math, Input, Type Conversion  

**🧠 Task:**  
একটি প্রোগ্রাম লিখুন যা ইউজারের কাছ থেকে বৃত্তের radius ইনপুট নেবে,  
তারপর area of circle বের করবে।  

**🧮 Formula:**  
Area = π × r²

markdown
Copy code

**💡 Hint:**  
- `import math` করে `math.pi` ব্যবহার করুন  
- Square বের করুন `r * r` বা `r**2` দিয়ে  

**🧩 Example:**
Enter radius: 5
Area of circle is: 78.54

markdown
Copy code

**🔍 Trick:**  
সবসময় সঠিক formula ব্যবহার করুন, এবং `math.pi` ব্যবহার করলে ফলাফল আরও নির্ভুল হবে।

---

### 🟢 Problem 3: Find the Largest Number 🏆  
**Topic:** Conditional Statements  

**🧠 Task:**  
একটি প্রোগ্রাম লিখুন যা ইউজারের কাছ থেকে তিনটি সংখ্যা ইনপুট নেবে  
এবং কোনটি সবচেয়ে বড় তা নির্ণয় করবে।  

**💡 Hint:**  
- তিনটি ইনপুট নিন — `a`, `b`, `c`  
- `if`, `elif`, `else` ব্যবহার করে তুলনা করুন  
- সবচেয়ে বড় সংখ্যাটি প্রিন্ট করুন  

**🧩 Example:**
Enter first number: 10
Enter second number: 25
Enter third number: 7
The largest number is: 25

markdown
Copy code

**🔍 Trick:**  
`if a > b and a > c:` — এইভাবে multiple condition combine করতে পারেন।

---

### 🟢 Problem 4: Even or Odd Checker 🔢  
**Topic:** Condition, Modulus Operator  

**🧠 Task:**  
একটি প্রোগ্রাম লিখুন যা ইউজারের কাছ থেকে একটি সংখ্যা ইনপুট নেবে,  
তারপর বলবে সংখ্যাটি Even না Odd।  

**💡 Hint:**  
- `%` অপারেটর দিয়ে ২ দিয়ে ভাগ করলে বাকি থাকে কি না তা যাচাই করুন  
- যদি `num % 2 == 0` হয় → Even  
- অন্যথায় → Odd  

**🧩 Example:**
Enter a number: 11
11 is an Odd number.

markdown
Copy code

**🔍 Trick:**  
এই ধরনের সমস্যায় সবসময় ভাবুন: “Divide করলে remainder 0 হয় নাকি?”

---

## 📤 Submission Rules

- প্রতিটি প্রোগ্রামে **comment লিখুন** যেন বোঝা যায় আপনি কী করছেন  
- **মোট মার্ক:** ১০০  
  - ৪টি প্রব্লেম × ২৫ মার্ক = ১০০ মার্ক  
- **Deadline:** ১ দিন —  
  ⏰ ২৮ অক্টোবর রাত ৯:০০ থেকে ২৯ অক্টোবর রাত ৯:০০ পর্যন্ত  
- নির্ধারিত সময়ের পরে সাবমিট করলে টোটাল মার্ক থেকে **৫ নম্বর কমে যাবে।**  
- কোড সাবমিট করার ৫–৬ দিনের মধ্যে মার্কস ইমেইলের মাধ্যমে দেওয়া হবে।  

📎 **Submit Here:**  
👉 [Google Form Link](https://docs.google.com/forms/d/e/1FAIpQLSf-PYVx7Y6pvCJLhL0NROoVD2WphV-XPquf6zfjjQ0kPYR63Q/viewform)
