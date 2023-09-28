with open('file2_w.txt', 'w') as f:
    f.write('New text space.....\n\n')
    f.write('Hey! This is Rayhan Khan')
    f.write("\nI am learning Computer Programming")
    f.write('\n\n')

#copy the file from one file to file2_w
with open('file.txt', 'r') as rf:
    with open('file2_w.txt', 'a') as af:
        for line in rf:
            af.write(line)

#operate with image
with open('image.png', 'br') as br: #image open in binary mode
    with open('image_copy.png', 'bw') as bw:
        for imagess in br:
            bw.write(imagess)