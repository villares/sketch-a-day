from pathlib import Path
import imageio

input_dir = Path.cwd()
images = [imageio.v3.imread(file_path)
                  for file_path in sorted(input_dir.iterdir())
                  if file_path.suffix.lower() == '.png']
if images:
    output_path = input_dir / 'output2.gif'
    imageio.v3.imwrite(
        output_path,
        images,
        duration=200,
        loop=0,
        )
