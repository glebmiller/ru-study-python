class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        def max_value(searched_list: list[int]) -> int:
            res = -(10**6)
            for i in searched_list:
                if i > res:
                    res = i
            return res

        if not input_list:

            return input_list
        else:
            max_int = max_value(input_list)
            input_list = list(map(lambda x: x if x < 0 else max_int, input_list))
            return input_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        def search(arr, low, high, x):

            # Check base case
            if high >= low:
                mid = (high + low) // 2

                # If element is present at the middle itself
                if arr[mid] == x:
                    return mid

                # If element is smaller than mid, then it can only
                # be present in left subarray
                elif arr[mid] > x:
                    return search(arr, low, mid - 1, x)

                # Else the element can only be present in right subarray
                else:
                    return search(arr, mid + 1, high, x)

            else:
                # Element is not present in the array
                return -1

        return search(input_list, 0, len(input_list) - 1, query)
