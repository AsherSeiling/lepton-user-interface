echo "Starting compalation"
cd lepton
mkdir -p build
cd build
cmake ..
make -j8
echo "Finished comparlarion"