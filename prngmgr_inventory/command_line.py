from prngmgr_inventory import inventory, parser


def main():
    args = parser.Parser().args
    output = inventory.Inventory(args=args).output
    print output

if __name__ == "__main__":
    main()
