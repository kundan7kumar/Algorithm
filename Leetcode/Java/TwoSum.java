
public class TwoSum {
	public static void TwoSum(int[] A,int sum)
	{
		
		for (int i=0; i <A.length-1; i++)
		{
			for (int j=i+1; j<A.length;j++)
			{
				if(A[i]+A[j]==sum)
				{
					System.out.println("Two Sum Pair:"+ i+"\t"+j);
					return;
				}
			}
		}
		System.out.println("Pair Not Found");
	}



public static void main(String[] args)
{
	int A[]={8,7,2,5,3,1};
	int sum=10;
	TwoSum(A,sum);
	
	
	}
}