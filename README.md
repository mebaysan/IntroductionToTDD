[![CI - Main](https://github.com/mebaysan/IntroductionToTDD/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/mebaysan/IntroductionToTDD/actions/workflows/ci.yaml) [![CI - Develop](https://github.com/mebaysan/IntroductionToTDD/actions/workflows/ci-dev.yaml/badge.svg?branch=develop)](https://github.com/mebaysan/IntroductionToTDD/actions/workflows/ci-dev.yaml)

# Introduction

This repo is designed to experiment TDD for my YouTube channel, [BaysanSoft](https://www.youtube.com/c/BaysanSoft).

Because of I am not a fan of Flask, I didn't pay attention to create a well-designed project structure. You can ask that "what is happening in create_app function?". I just try to keep it simple.

You can access the presentation files by [here](https://www.canva.com/design/DAFv8eCNMN4/Z498h5Wz9hxSmYcAwI0mng/watch?utm_content=DAFv8eCNMN4&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink).

You can access the video on YouTube by [here](https://youtu.be/A0GnGWw5TW0).

Kind regards


# Introduction to TDD (Test Driven Development)

- In TDD, test cases drive code design.
- The Red/Green/Refactor workflow includes three steps:
  - Write a failing unit test case for the code you wish you had
  - Write just enough code to pass this test case
  - Refactor the code to improve its quality
- TDD saves development time and ensures that the code works as expected.
- To create a DevOps pipeline, you must automate all testing.
- The xUnit series is one of the most popular testing frameworks for TDD, while others include Jasmine for JavaScript, Mocha for Node.js, and SimpleTest for PHP.
- The two most popular testing frameworks for Python are PyUnit and Pytest.
- Test fixtures establish a known initial state before and after each test.
- Test fixtures are helpful for many testing situations such as creating mock objects and loading a database with a known set of data.
- The higher the test coverage, the more confident developers can be that their code works as expected.
- Missing test coverage reports can help developers identify lines of code that still need test cases.
- Factories and fakes are useful for creating and maintaining a large amount of test data.
  - Factories generate fakes with realistic test data.
  - Fakes behave like real objects during testing, so developers test fakes like they test real data.
- **Mocking is a process for creating objects that mimic the behavior of real objects.**
- Developers should mock whenever they want to isolate tests from a remote component or external system.
- **Patching is a mocking technique by which developers change the behavior of a function call.**
- Mock objects are objects that mimic the behavior of real objects in ways that you can control.

# Run with Docker

```bash
docker image build . -t myapp-local:latest

docker run -p 8000:5000 -d --name myapp-local myapp-local:latest
```
