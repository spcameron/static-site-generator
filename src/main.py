from textnode import TextNode, TextType


def main():
    test_node = TextNode("This is some anchor text", TextType.IMAGE, "https://google.com")
    print(test_node)

if __name__ == "__main__":
    main()