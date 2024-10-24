def NULL_not_found(object: any) -> int:
    object_name = object.__class__.__name__

    match object_name:
        case 'NoneType':
            print("Nothing:", object, object.__class__)
        case 'float':
            print("Cheese:", object, object.__class__)
        case 'int':
            print("Zero:", object, object.__class__)
        case 'str' if len(object) == 0:
            print("Empty:", object, object.__class__)
        case 'bool':
            print("Fake:", object, object.__class__)
        case _:
            print("Type not Found")
            return 1
    return 0
