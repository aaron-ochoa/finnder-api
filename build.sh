BUILD_DIR=temp
CORE_LIB_DIR=finnlib
JOB_FILE_NAME=handler
AWS_LAMBDA_FILENAME=lambda_function
JOB_FILE_NAME=finnder

JOB_FILE="$JOB_FILE_NAME.py"
JOB_ZIP_FILE="$JOB_FILE_NAME.zip"

# Create a temp directory to use
# for building the project
if [ -d $BUILD_DIR ]; then
  rm -r $BUILD_DIR/*
else
  mkdir $BUILD_DIR
fi

# Copy all package files from pip and
# src files into build dir
cp -R venv/lib/python3.6/site-packages/. $BUILD_DIR
rm $BUILD_DIR/easy_install.py
cp -R $CORE_LIB_DIR $BUILD_DIR

# Copy the job file into the build dir and rename
cp $JOB_FILE $BUILD_DIR
mv "$BUILD_DIR/$JOB_FILE" "$BUILD_DIR/$AWS_LAMBDA_FILENAME.py"

# Remove old zip file - if any
if [ -f "dist/$JOB_ZIP_FILE" ]; then
  rm "dist/$JOB_ZIP_FILE"
fi

# Go into the build dir and make the zip
cd $BUILD_DIR
zip --quiet -r $JOB_ZIP_FILE *
cd ..

# Copy the created zip file up into the root dir
cp "$BUILD_DIR/$JOB_ZIP_FILE" dist/

# Clean up
rm -rf $BUILD_DIR

echo "Built successfully"
