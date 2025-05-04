import OpenEXR

def LoadLUT(self, filepath):
    infile = OpenEXR.File(filepath)
    part = infile.parts[0]
    height = part.height()
    width = part.width()

    for name,channel in part.channels.items():
        print(name, channel, channel.pixels.shape, channel.pixels.dtype)

    rgba_data = infile.channels()["RGBA"].pixels
    for row in range(len(rgba_data)):
        for column in range(len(rgba_data[row])):
            if column == 0:
                rgba_data[row][column][0] = 0
                print(rgba_data[row][column])

    # header = infile.header()
    # new_channels = {"RGBA": rgba_data}
    # with OpenEXR.File(header, new_channels) as outfile:
    #     outfile.write("modified.exr")