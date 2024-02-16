## Pathlib
Class based filesystem paths

### Properties
- p.parts
- p.root
- p.anchor
- p.parent
- p.parents _returns list of path objects of all parents_
- p.name _Name of the leaf file/dir_
- p.suffix
- p.suffixes
- p.as_uri

### Methods
- p.is_dir()
- p.exists()
- p.is_file()
- p.is_absolute()
- p.resolve()
- p.cwd()
- p.home()
- p.mkdir()
- p.match("pattern")
- p.glob(pattern, *, case_sensitive=None)
- p.rglob() -Same as calling glob recursively '**/'-
- p.iterdir() _yeilds path objects of the directory_
- p.walk() _python 3.12+ generates dirpath, dirnames, filenames in the directory tree_
- p.open() _readline() after the file is open_
- p.read_text()
- p.rmdir() _Removes an empty directory_
- p.touch()