from post import Address
from post import Mailing

to = Address("125167", "Mosсow", "Leningradskiy prospekt", "39", "79")
froms = Address("109004", "Mosсow", "Alexandra Solzhenitsyn", "23a", "3")
to.postAddress() 
froms.postAddress()

address2 =to.postAddress()
address1 =froms.postAddress()

mail = Mailing(address2, address1, "1000", "LC05LOX87CN")
mail.postTrack()