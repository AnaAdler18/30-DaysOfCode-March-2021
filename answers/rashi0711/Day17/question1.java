import java.util.Scanner;

public class uniquequadruple {

	public static void main(String[] args) {
		int n;
		Scanner sc=new Scanner(System.in);
		n=sc.nextInt();
		int arr[]=new int[n];
		for(int i=0;i<n;i++)
		{
			arr[i]=sc.nextInt();
			
		}
		int num=sc.nextInt();
		for(int i=0;i<n-3;i++)
		{
			for(int j=i+1;j<n-2;j++)
			{
				for(int k=j+1;k<n-1;k++)
				{
					for(int l=k+1;l<n;l++)
					{
						
						if(arr[i]+arr[j]+arr[k]+arr[l]==num)
						{
							System.out.println(arr[i]+" "+arr[j]+" "+arr[k]+" "+arr[l]);
						}
						
					}
				}
			}
		}

	}

}
