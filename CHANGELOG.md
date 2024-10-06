# Changelog
This file documents all significant changes made to this chess project.

## [v0.3.1] - 2024-10-06
- Reorganized the main file for TestCoverage reasons.
- Comments were added again in the codes.
- Added more tests for Test coverage reasons. 
- Updated prefixes and suffixes ( “__” ) in Attributes.

## [v0.3.0] - 2024-10-03
#### Added
- PyGame fully functional removed from main
- Test coverage was modified
- English translation added
- Redis update


## [v0.2.9] - 2024-10-02
#### Added
- Updated a Console print and retested all files.
- Updated CircleCI configuration (REDIS installation)


## [v0.2.8] - 2024-10-01
#### Added
- Updated main code corresponding to the screenshots shown in the terminal.
- Updated King code
- Added local game save via ID in Redis
- Reverted to the original .codeclimate.yml


## [v0.2.7] - 2024-09-10
#### Added
- Added new tests for main.py and board.py
- Updated and corrected the comments with their respective title in all codes
- Fixed the location of the images in the code made in pygame


## [v0.2.6] - 2024-09-09
#### Added
- Removed main and board tests due to errors with their execution.


## [v0.2.5] - 2024-09-08
#### Added
- SOLID principles for main.py and board.py
- Part scores
- Message when deleting part


#### Coming soon
- Test update for main and board


## [v0.2.4] - 2024-09-07
#### Added
- added more comments in the code operation for chess in console
- added chess with pygame graphical interface without modular because it is not responding as expected locally.


## [v0.2.3] - 2024-09-06
#### Added


- Added comments on the code operation.
- Updated the main README


## [v0.2.2] - 2024-09-05
#### Added


- Improved the logic of the Queen part
- Added tests for main.py and piece.py


## [v0.2.1] - 2024-09-04
#### Added


- Fixed tests and configurations for Circleci to run properly


## [v0.2.0] - 2024-09-03
#### Added


- Added a new branch with the pygame code


#### Modified


- Modified the main branch
- Updated the files in a modular way and for more readability


## [v0.1.9] - 2024-09-02
#### Added
- Reorganized and updated the order of Pygame folder


## [v0.1.8] - 2024-09-1
#### Added
- Added new tets and tested them for Console Chess


## [v0.1.7] - 2024-08-31
#### Added
- Updated the Chess code in console and tests.
- Updated CHANGELOG.md formatting


## [v0.1.6] - 2024-08-30
#### Added
- Chess reorganization folders were created for better readability and performance




## [v0.1.5] - 2024-08-29
### Added
- Added the feet and check the proper functioning of the app


## [v0.1.4] - 2024-08-28
### Added
- Added the seeds to run the chess project through the console




## [v0.1.3] - 2024-08-26
### Added
- Updated main.py adding event handling, main game loop, blinking square around king if in check, “game over” message and restart option,


### Modified
- Updated the organization of the project as well as the comments in the code to know how each line works.


### Fixed
- Minor bug fixes.


## [v0.1.2] - 2024-08-25
### Added
- Updated the main.py adding movements and constraints of the pieces.


### Modified
- Updated the project organization.


## [v0.1.1] - 2024-08-24


### Added
- Added images of the parts in the repository and in the code.
- Added tested tests with the finished project in Local.


### Modified
- Updated the project organization.


### Modified
- Minor bug fixes.




## [v0.1.0] - 2024-08-23


### Added earlier
- Initial Pygame configuration for main game window.
- CircleCI configuration for continuous integration and automatic testing on each commit.
- Creation of README file with detailed instructions for installation, execution and contribution to the project.


### Added
- Defined key variables for dashboard state management and game flow control.
- Added Dockerfile to containerize the application and facilitate its deployment in different environments.
- CHANGELOG


### Modified
- Updated the project organization to facilitate future expansions.


### Fixed
- Minor bug fixes related to Pygame initialization.


### Coming soon
- Implemented game logic, including move validation and check and checkmate detection.
- Improved user interface and game experience.
- An artificial intelligence for play against the computer.
