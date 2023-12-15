def longest_word(input_str):
    words = input_str.split()
    longest =max(word, key=len)
    return longest
    input1 ="dummy text of the printing and typesetting industry."
    output1 =longest_word(input1)
    print(output)

    input2 ="It is a long-established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distributionqqqqqqqqqqqqqqqqqqq of letters, as opposed to using 'Content here, content here', making it look like readable English"
    output2 =longest_word(input2)
    print(output2)