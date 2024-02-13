## Capital One

### online tech screen
1. max and current ratings
2. panel codes index pattern
3. 2xN matrix array order by "beauty"
4. binary string count and flip

### power day
- coding challenge
- system design
- behavioral
- case
- director

## Datadog
### first round
1. total repetitions in paragraph
2. find_max_points in trie Milestone(points, children)

### virtual onsite
- coding challenge x 2
- system design
- behavioral
- systems (discussion)

### notes
- [coderpad](https://coderpad.io)
- [excalidraw](https://excalidraw.com)
- code challenge 1 - file system
  1. `File` class with `write` method
  2. implement `BufferedFile` class
  3. extension: base write method is changed:
     - writes random number of inputted bytes; at least 1
     - returns number of successfully written bytes
- code challenge 2 - file system
  - `fs.List` returns array of **absolute** paths within a directory
  - paths are either files or directories
  - `fs.Delete` removes either a single file or an empty directory
  - `fs.isDirectory` checks if the path is a directory
  - implement the function equivalent of `rm -rf`
  - discuss spacetime complexity
  - optimizations in recursive approach:
    - consider `fs.List` could return many file paths compared to directories
    - reduce the list size before next recursion cycle by filtering paths that are directories
    - reduce memory by shrinking the list while you traverse it
    - reduce memory by only string the relative paths
      - the absolute path can be inferred before calling the next recursive function
- system design - flight deals
  - external apis to check price for trip from source to destination for a few platforms
  - users want to tell the system about their trip, and receive a notification within 10 minutes of a discount
  - data science team created machine learning model that checks if a trip is discounted
  - support 10 million users
