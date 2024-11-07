def all_thing_is_obj(object: any) -> int:
    object_name = object.__class__.__name__

    match object_name:
        case 'list':
            print("List :", object.__class__)
        case 'tuple':
            print("Tuple :", object.__class__)
        case 'set':
            print("Set :", object.__class__)
        case 'dict':
            print("Dict :", object.__class__)
        case 'str':
            print(object, "is in the kitchen :", object.__class__)
        case _:
            print("Type not found")

    return 42
