def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9995
   if obj[3] == 'Sell':
      # Feature: Closing, Instances: 61, Entropy: 0.9127
      if obj[0]<=775.47998:
         # Feature: SMA2, Instances: 55, Entropy: 0.9457
         if obj[5] == 'Sell':
            # Feature: RSI, Instances: 30, Entropy: 0.7838
            if obj[1] == 'Hold':
               # Feature: SMA1, Instances: 27, Entropy: 0.8256
               if obj[4] == 'Buy':
                  # Feature: MACD, Instances: 15, Entropy: 0.7219
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  # Feature: MACD, Instances: 12, Entropy: 0.9183
                  if obj[2] == 'Buy':
                     return 'No'
                  elif obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[1] == 'Buy':
               return 'No'
            else:
               return 'No'
         elif obj[5] == 'Buy':
            # Feature: SMA1, Instances: 25, Entropy: 0.9988
            if obj[4] == 'Buy':
               # Feature: MACD, Instances: 18, Entropy: 0.9641
               if obj[2] == 'Sell':
                  # Feature: RSI, Instances: 17, Entropy: 0.9367
                  if obj[1] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               # Feature: MACD, Instances: 7, Entropy: 0.8631
               if obj[2] == 'Buy':
                  # Feature: RSI, Instances: 5, Entropy: 0.971
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'Yes'
      elif obj[0]>775.47998:
         return 'No'
      else:
         return 'No'
   elif obj[3] == 'Hold':
      # Feature: MACD, Instances: 49, Entropy: 0.73
      if obj[2] == 'Buy':
         # Feature: Closing, Instances: 42, Entropy: 0.7919
         if obj[0]<=775.47998:
            # Feature: SMA2, Instances: 41, Entropy: 0.7593
            if obj[5] == 'Buy':
               # Feature: RSI, Instances: 34, Entropy: 0.6723
               if obj[1] == 'Hold':
                  # Feature: SMA1, Instances: 21, Entropy: 0.7919
                  if obj[4] == 'Buy':
                     return 'Yes'
                  elif obj[4] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[1] == 'Sell':
                  # Feature: SMA1, Instances: 13, Entropy: 0.3912
                  if obj[4] == 'Buy':
                     return 'Yes'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               # Feature: RSI, Instances: 7, Entropy: 0.9852
               if obj[1] == 'Hold':
                  # Feature: SMA1, Instances: 5, Entropy: 0.7219
                  if obj[4] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[1] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'Yes'
         elif obj[0]>775.47998:
            return 'No'
         else:
            return 'No'
      elif obj[2] == 'Sell':
         return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      return 'No'
   else:
      return 'No'
