import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Test {

    public static List<Integer> al;

    public static void printMaxOfMin(int n) {
        int max = 0;

        for (int i = 0; i <= al.size() - n; i++)
        {
            int mini = Integer.MAX_VALUE, j = i;
            int c = n;
            while(c > 0)
            {
                mini = Math.min(mini, al.get(j));
                j++;
                c--;
            }
            System.out.println("mini is  : " + mini);
            max = Math.max(max, mini);
        }

        System.out.printf("max is : " + max);
    }



        // Used to find previous and next smaller
//        Stack<Integer> s = new Stack<>();
//
//        // Arrays to store previous and next smaller
//        int left[] = new int[n+1];
//        int right[]  = new int[n+1];
//
//        // Initialize elements of left[] and right[]
//        for (int i=0; i<n; i++)
//        {
//            left[i] = -1;
//            right[i] = n;
//        }
//
//        // Fill elements of left[] using logic discussed on
//        // https://www.geeksforgeeks.org/next-greater-element/
//        for (int i=0; i<n; i++)
//        {
//            while (!s.empty() && arr[s.peek()] >= arr[i])
//                s.pop();
//
//            if (!s.empty())
//                left[i] = s.peek();
//
//            s.push(i);
//        }
//
//        // Empty the stack as stack is going to be used for right[]
//        while (!s.empty())
//            s.pop();
//
//        // Fill elements of right[] using same logic
//        for (int i = n-1 ; i>=0 ; i-- )
//        {
//            while (!s.empty() && arr[s.peek()] >= arr[i])
//                s.pop();
//
//            if(!s.empty())
//                right[i] = s.peek();
//
//            s.push(i);
//        }
//
//        // Create and initialize answer array
//        int ans[] = new int[n+1];
//        for (int i=0; i<=n; i++)
//            ans[i] = 0;
//
//        // Fill answer array by comparing minimums of all
//        // lengths computed using left[] and right[]
//        for (int i=0; i<n; i++)
//        {
//            // length of the interval
//            int len = right[i] - left[i] - 1;
//
//            // arr[i] is a possible answer for this length
//            // 'len' interval, check if arr[i] is more than
//            // max for 'len'
//            ans[len] = Math.max(ans[len], arr[i]);
//        }
//
//        // Some entries in ans[] may not be filled yet. Fill
//        // them by taking values from right side of ans[]
//        for (int i=n-1; i>=1; i--)
//            ans[i] = Math.max(ans[i], ans[i+1]);
//
//        // Print the result
//
//        int maxValue = Integer.MIN_VALUE;
//
//        for (int i=1; i<=n; i++)
//        {
//            maxValue = Math.max(maxValue, ans[i]);
//        }
//
//        System.out.printf("maxValue : " + maxValue);


    // Driver method
    public static void main(String[] args)
    {
       al = new ArrayList<>();
       al.add(10);
        al.add(20);
        al.add(30);
        al.add(50);
        al.add(10);
        al.add(70);
        al.add(30);

        printMaxOfMin(2);
    }
}