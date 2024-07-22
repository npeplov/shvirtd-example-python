GITHUB_USERNAME="npeplov"
REPO_NAME="shvirtd-example-python.git"
TARGET_DIR="/opt/$REPO_NAME"

if [ -d "$TARGET_DIR" ]; then
  echo "Каталог $TARGET_DIR уже существует. Программа завершает работу."
else
  git clone "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git" "$TARGET_DIR"
fi

cd "$TARGET_DIR"
docker compose up -d