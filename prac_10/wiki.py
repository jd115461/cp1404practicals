import wikipedia


def main():
    """Prompt the user for a page title, show summary, handle errors."""
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title)
            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        title = input("\nEnter page title: ").strip()
    print("Thank you.")


if __name__ == "__main__":
    main()
