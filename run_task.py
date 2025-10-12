from tasks import long_running_timeout


def main() -> None:
    # Enqueue a task that will exceed the configured time limits
    async_result = long_running_timeout.delay(60)
    print(async_result.id)


if __name__ == "__main__":
    main()
