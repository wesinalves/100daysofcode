# This command optimizes for Intel’s Broadwell processor
bazel build -c opt --copt=-march="broadwell" 
--config=cuda //tensorflow/tools/pip_package:build_pip_package
