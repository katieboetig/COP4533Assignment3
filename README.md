# COP4533Assignment3

Question 1:

All resulting data is int he "results.txt" file, and then that data was transferred into the "plot_graph.py" file. To rebuild, run the following:

python data/plot_graph.py

That will create a new png, but for your convience, this has already been created and uploaded (runtime_analysis.png) to the repository. 


Run all tests at once: for i in {1..10} do echo "test$i" time python src/hvlcs.py < tests/test$i.in > tests/test$i.out done

Single Test: time python src/hvlcs.py < tests/example.in > tests/example.out

note: "python3" might need to replace "python" if working on MacOS.
