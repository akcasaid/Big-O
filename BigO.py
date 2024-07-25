def example_function(arr):
    # Başlangıçtaki bir adım, bu O(1)'dir.
    n = len(arr)  # Liste uzunluğunu bulmak O(1)'dir.

    # Döngünün başlangıcı, bu döngü O(n) olacaktır çünkü i her değeri 0'dan n-1'e kadar alır.
    for i in range(n):
        # Döngü içinde bir adım, bu O(1)'dir.
        print("Element:", arr[i])

    # İç içe iki döngü, dış döngü O(n) ve iç döngü de O(n) olacaktır.
    # Toplamda bu kısmın karmaşıklığı O(n^2)'dir.
    for i in range(n):
        for j in range(n):
            # İç içe döngülerin içinde sabit bir işlem, bu O(1)'dir.
            print("Pair:", arr[i], arr[j])

    # Döngüde ikili arama, her bir ikili arama O(log n) olduğu için, bu kısım O(n log n)'dir.
    for i in range(n):
        binary_search(arr, arr[i])  # binary_search fonksiyonu O(log n)'dir.

    # Son adımda tüm işlemleri toplarsak: O(n) + O(n^2) + O(n log n) olur.
    # En büyük terim dominant olduğu için, bu fonksiyonun toplam karmaşıklığı O(n^2)'dir.
    return

def binary_search(arr, x):
    # Bu fonksiyonun karmaşıklığı O(log n)'dir.
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # x middeki eleman ise
        if arr[mid] < x:
            low = mid + 1

        # x middeki elemandan küçükse
        elif arr[mid] > x:
            high = mid - 1

        # x middeki elemana eşitse
        else:
            return mid

    # Eğer x listede yoksa
    return -1


if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 5]
    example_function(test_array)
