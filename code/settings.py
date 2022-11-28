# game setup
WIDTH = 1280
HEIGTH = 720
FPS = 60
TILESIZE = 64

# Testmap for rendering level. to be replaced with layered csvs in the future...dont ask me how though

TEST_MAP = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", "-", " ", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", "-", " ", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", "p", " ", " ", " ", " ", " ", " ", "-", " ", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", "-", " ", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", "-", "-", "-", "-", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", "-", "-", "-", "-", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
]

ITEMS = ["desk",
         "chair",
         "coffee",
         "cup",
         "laptop",
         "plant",
         "monitor",
         "mouse",
         "keyboard",
         "tv",
         "table",
         "door",
         "window",
         "developer",
         "filing cabinet",
         "cabinet",
         "server",
         "lamp"]