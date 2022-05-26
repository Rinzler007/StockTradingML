def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9973
   if obj[3] == 'Sell':
      # Feature: Closing, Instances: 72, Entropy: 0.9726
      if obj[0]>5.324:
         # Feature: RSI, Instances: 67, Entropy: 0.9869
         if obj[1] == 'Hold':
            # Feature: SMA2, Instances: 65, Entropy: 0.9916
            if obj[5] == 'Sell':
               # Feature: SMA1, Instances: 38, Entropy: 0.9678
               if obj[4] == 'Sell':
                  # Feature: MACD, Instances: 20, Entropy: 0.971
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[4] == 'Buy':
                  # Feature: MACD, Instances: 18, Entropy: 0.65
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Buy':
               # Feature: SMA1, Instances: 27, Entropy: 0.999
               if obj[4] == 'Buy':
                  # Feature: MACD, Instances: 21, Entropy: 0.9587
                  if obj[2] == 'Sell':
                     return 'Yes'
                  elif obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[4] == 'Sell':
                  # Feature: MACD, Instances: 6, Entropy: 0.65
                  if obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'Yes'
         elif obj[1] == 'Buy':
            return 'No'
         else:
            return 'No'
      elif obj[0]<=5.324:
         return 'No'
      else:
         return 'No'
   elif obj[3] == 'Hold':
      # Feature: RSI, Instances: 38, Entropy: 0.6292
      if obj[1] == 'Hold':
         # Feature: SMA1, Instances: 23, Entropy: 0.8281
         if obj[4] == 'Buy':
            # Feature: MACD, Instances: 21, Entropy: 0.7025
            if obj[2] == 'Buy':
               # Feature: Closing, Instances: 14, Entropy: 0.7496
               if obj[0]>5.324:
                  # Feature: SMA2, Instances: 14, Entropy: 0.7496
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[2] == 'Sell':
               # Feature: Closing, Instances: 7, Entropy: 0.5917
               if obj[0]>5.324:
                  # Feature: SMA2, Instances: 7, Entropy: 0.5917
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[4] == 'Sell':
            return 'No'
         else:
            return 'No'
      elif obj[1] == 'Sell':
         return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      return 'No'
   else:
      return 'No'
