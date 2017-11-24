# Arrange
cp $HOME/.gitconfig .
export HOME=$PWD
echo "home is: " $HOME

# Act
git-phlow auth

# Assert
git config --show-origin --global --list
