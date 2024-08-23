# Build a Static Site Generator project

Personal solution to the [Build a Static Site Generator project](https://www.boot.dev/courses/build-static-site-generator) from [Boot.dev](https://www.boot.dev/tracks/backend).

## Requirements

- Python (3.12+)

## Set up

1. Open your terminal from the project's root directory.
2. Run the following command to generate static content and start the server:

    ```sh
    ./main.sh
    ```

3. Visit the website at http://[::]:8888/.

## Running tests

This project uses the [`unittest` testing framework](https://docs.python.org/3/library/unittest.html) from Python's standard library to run unit tests. Each test case is located within its own `test_<case>.py` file within the `tests/` directory.

To run all tests, run the following command from the project's root:

```sh
./test.sh
```
