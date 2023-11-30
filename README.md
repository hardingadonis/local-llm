# Local LLM
![GitHub top language](https://img.shields.io/github/languages/top/hardingadonis/local-llm)
![GitHub repo size](https://img.shields.io/github/repo-size/hardingadonis/local-llm)
![GitHub License](https://img.shields.io/github/license/hardingadonis/local-llm)
> A local LLM chatbot

## Preview
<img src="imgs/preview-1.png" alt="Preview Image 1"/>
<img src="imgs/preview-2.png" alt="Preview Image 2"/>
<img src="imgs/preview-3.png" alt="Preview Image 3"/>

## Requirements
- Python 3
- `virtualenv` package

## Installation
- Clone repository
```bash
git clone https://github.com/hardingadonis/local-llm.git
cd local-llm/
```

- Create virtual environment
```bash
virtualenv .venv
```

- Activate virtual environment
```bash
"./.venv/Scripts/activate"
```

- Install dependencies
```bash
pip install -r requirements.txt
```

- Download models
```bash
python server/download_models.py
```

- Run application
```bash
python server/run_server.py
```

## Notes:
- You can download other models. Just make sure to put them in the `server/models` directory.

## Contributors:

<a href="https://github.com/hardingadonis/local-llm/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=hardingadonis/local-llm" />
</a>

## Licenses:
- [Local LLM](https://github.com/hardingadonis/local-llm) is under the [MIT license](https://github.com/hardingadonis/local-llm/blob/main/LICENSE).