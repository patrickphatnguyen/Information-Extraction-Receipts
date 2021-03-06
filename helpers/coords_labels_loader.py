def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)


def load_from_path(labels_path):
  list_coords = []
  list_labels = []

  with open(labels_path,"r") as f:
    lines = f.readlines()

    for line in lines:
      # find the comma that split between coords with labels
      last_comma = findnth(line, ',', 7)

      line  = line.replace("\n","")
      coords = line[:last_comma].split(",")
      label = line[last_comma+1:].replace("\n","")

      bbox = {}
      bbox["x_min"] = int(coords[0])
      bbox["y_min"] = int(coords[1])
      bbox["x_max"] = int(coords[4])
      bbox["y_max"] = int(coords[5])

      list_coords.append(bbox)
      list_labels.append(label)

  return list_coords,list_labels
