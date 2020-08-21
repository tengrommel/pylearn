# Introduction

# 1.1 Variables
> Before going to definition of variables, let us relate them to old mathematical 
All of us have solved many mathematical equations since childhood. 

We don't have to worry about the use of this equation. The important thing we need to understand is
that the equation has names(x and y), which hold values (data). That means the names (x and y) are 
placeholders for representing data.

Similarly, in computer science programming we need something for holding data, and variables
is the way to do that.

# 1.2 Data Types
> In the above-mentioned equation, the variables x and y can take any value such as integral numbers (10, 20),
real numbers (0.23, 5.5), or just 0 and 1. To solve the equation, we need to relate them to the kind of values 
they can take, and data type is the name used in computer science programming for this purpose. A data type in 
a programming language is a set of data with predefined values.

- System-defined data types(also called Primitive data types)
> Data types that are defined by system are called primitive data types. The primitive data types provided by 
Go programming language are: int (platform dependent), int32, int64, float32, float64, byte, bool, etc. The number
 of bits allocated for each primitive data type depends on the programming languages, the compiler and the operating 
system. For the same primitive data type, different languages may use different sizes. Depending on the size of the 
data types, the total available values(domain) will also change.

The int, uint, and uintptr types are usually 32 bits wide on 32-bit systems and 64 bits wide on 64-bit systems.
The number of bits allocated for each primitive data type depends on the programming languages, the compiler and 
the operating system. For the same primitive data type, different languages may use different sizes. Depending on 
the size of the data types, the total available values(domain) will also change.

The int, uint, and uintptr types are usually 32 bits wide on 32-bit systems and 64 bits wide on 64-bit systems.
When you need an integer value you should use int unless you have a specific reason to use a sized or unsigned 
integer type.

- User-defined data types
> If the system-defined data types are not enough, then most programming languages allow the users to define their 
own data types, called user - defined data types. Good examples of user defined data types are: structures in Go 
language and classes in Java, C++, and Python. For example, in the snippet blow, we are combining many system-defined 
data types and calling the user defined data type by the name "NewType".
    
    type NewType struct {
        data1 int
        float32 data2
        ...
        data interface{} // generic data type
    }

1.3 Data structures
> Based on the discussion above, once we have data in variables, we need some mechanism for manipulating that data 
to solve problems. Data structure is a particular way of storing and organizing data in a computer so that it can 
be used efficiently.

A data structure is a special format for organizing and storing data. General data structure types include arrays, 
files, linked lists, stacks, queues, trees, graphs and so on.

Depending on the organization of the elements, data structures are classified into two types:

- Linear data structures: Elements are accessed in a sequential order but it is not compulsory to store all elements 
sequentially. Examples: Linked Lists, Stacks and Queues.
- Non-linear data structures: Elements of this data structure are stored/accessed in a non-linear order. 
Examples: Trees and graphs