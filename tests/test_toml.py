import pyhelios
import pyhelios.toml


def test_toml_read_write(tmp_path):
    dw = {"hello": "world"}
    fn = tmp_path / "hello.toml"
    pyhelios.toml.write(dw, fn)
    dr = pyhelios.toml.read(fn)
    assert dw == dr


def test_toml_read_write_table(tmp_path):
    dw = {"person": {}}
    dw["person"]["first"] = {
        "first_name": "John",
        "last_name": "Doe",
        "experience": [
            {"company": "Google", "duration": 10},
            {"company": "Facebook", "duration": 5},
        ],
    }
    dw["person"]["second"] = {
        "first_name": "Janie",
        "last_name": "Doe",
        "experience": [
            {"company": "Amazon", "duration": 1},
            {"company": "Apple", "duration": 20},
        ],
    }
    fn = tmp_path / "person.toml"
    pyhelios.toml.write(dw, fn)
    dr = pyhelios.toml.read(fn)
    assert dw == dr
