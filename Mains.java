class Pair< K extends Comparable<K> , V>
{
   K first;
   V second;

   Pair(K k,V v)
   {
        first=k;
        second=v;
   }

}


class PairNode< K extends Comparable<K> , V>
{
    Pair<K,V> data;
    PairNode<K,V> next;

    PairNode( Pair <K,V> f , PairNode<K,V> s)
    {
        data=f;
        next=s;
   }
}


class SortedChain< K extends Comparable<K> , V> 
{

    int dsize;
     PairNode<K,V> head;

      SortedChain( )
      {
           dsize=0;
           head=null;
        }


      
     public void insert(Pair<K,V> p, K key)
     {
         PairNode<K,V> npnode= new PairNode<K,V>(p,null);

          if(head==null)
          {
              head=npnode;
          }
          
        else
        {
             PairNode<K,V> prev=null;
            PairNode<K,V> temp=head;

            while( temp !=null  && p.First.compareTo(temp.data.first)>0)
              { 
                   prev=temp;
                   temp=temp.next;
              }

             if(temp !=null && (temp.data.first)==p.first)
             {
                  System.out.println("dup");
                }
              else
              {
                 npnode.next=temp;
                  if(prev==null)
                  {
                      head=npnode;
                   }

                  else
                  {
                      prev.next=npnode;
                   }

              }
       }
       }


     public void remove(Pair<K,V> p, K key)
     {
         //PairNode<K,V> npnode= PairNode<K,V>(p,null);

          if(head==null)
          {
              System.out.println("empty");
          }
          
        else
        {
             PairNode<K,V> prev=null;
            PairNode<K,V> temp=head;

            while( temp !=null  && key.compareTo(temp.data.first)>0)
              { 
                   prev=temp;
                   temp=temp.next;
              }

             if(temp==null)
             {
                  System.out.println("not found");
                }
              else if(key.compareTo(temp.data.first)<0)
              {
                    System.out.println("not found");
              }
              else
               {
                 
                  if(temp==head)
                  {
                      head=temp.next;
                   }

                  else
                  {
                      prev.next=temp.next;
                      System.out.println(temp.data);
                   }
        
              }
       }

}}

   class Mains
 {
        public static void main(String [] args)
       {
             SortedChain<Integer,String> s=new SortedChain<Integer,String>();

             Pair<Integer,String>p1=new Pair<Integer,String>(7,"seven");
               Pair<Integer,String>p1=new Pair<Integer,String>(2,"two");
             s.insert(p1);
              s.insert(p2);
              Pair<Integer,String>p1=new Pair<Integer,String>(3,"three");
              s.insert(p2);
          }
}
  


