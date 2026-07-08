def display_cube(cube):

    print()

    # Up face
    print("      " + cube["U"][0] + " " + cube["U"][1])
    print("      " + cube["U"][2] + " " + cube["U"][3])

    print()

    # Middle row
    print(
        cube["L"][0] + " " + cube["L"][1] + "   " +
        cube["F"][0] + " " + cube["F"][1] + "   " +
        cube["R"][0] + " " + cube["R"][1] + "   " +
        cube["B"][0] + " " + cube["B"][1]
    )

    print(
        cube["L"][2] + " " + cube["L"][3] + "   " +
        cube["F"][2] + " " + cube["F"][3] + "   " +
        cube["R"][2] + " " + cube["R"][3] + "   " +
        cube["B"][2] + " " + cube["B"][3]
    )

    print()

    # Down face
    print("      " + cube["D"][0] + " " + cube["D"][1])
    print("      " + cube["D"][2] + " " + cube["D"][3])

    print()
